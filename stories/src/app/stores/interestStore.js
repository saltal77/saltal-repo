import {
    ADD_INTEREST,
    GET_INTEREST_BEGIN,
    GET_INTEREST_END,

} from '../constants/interestConstants';

import dispatcher from '../dispatcher';
import axios from 'axios';

import { EventEmitter } from 'events';

class InterestStore extends EventEmitter {
    constructor()
    {
        super(...arguments);

        this.interestList = [];

        this.getInterestBegin = this.getInterestBegin.bind(this);
        this.getInterestEnd = this.getInterestEnd.bind(this);
        this.change = this.change.bind(this);
        this.showInterest = this.showInterest.bind(this);
        this.InterestStoreHandleActions = this.InterestStoreHandleActions.bind(this);
    }

    getInterestBegin(){
        axios
            .get('../data/interest_data.json')
            //.get('http://localhost:8888/store/listinterest')
            .then((response) => {
                let { data } = response;

                dispatcher.dispatch(
                    {
                        type: GET_INTEREST_END,
                        payload: data
                    }
                );
            });
    }

    getInterestEnd(interest)
    {
        this.interestList = interest;
        this.change();
    }

    change()
    {
        this.emit('change', this.interestList);
    }

    showInterest()
    {
        return this.interestList;
    }

    addInterest(interest)
    {
        this.interestList.push(interest);
        this.change();
    }


    InterestStoreHandleActions(action)
    {
        switch (action.type)
        {
            case ADD_INTEREST:
            {
                this.addInterest(action.payload);
                break;
            }
            case GET_INTEREST_BEGIN:
            {
                this.getInterestBegin();
                break;
            }
            case GET_INTEREST_END:
            {
                this.getInterestEnd(action.payload);
                break;
            }

        }
    }
}

const interestStore = new InterestStore;

dispatcher.register(interestStore.InterestStoreHandleActions);

export default interestStore;

