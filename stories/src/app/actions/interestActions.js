import dispatcher from '../dispatcher';
import {ADD_INTEREST, GET_INTEREST_BEGIN} from '../constants/interestConstants';

export function addInterest({title, text}) {
    const interest = {title, text};

    dispatcher.dispatch({
        type: ADD_INTEREST,
        payload: interest
    });
}

export function getInterest() {
    dispatcher.dispatch({
        type: GET_INTEREST_BEGIN
    });
}

