import {
    ADD_COMMENT,
    DEL_COMMENT,
    UPDATE_COMMENT,
    GET_COMMENTS_BEGIN,
    GET_COMMENTS_END,

} from '../constants/commentsConstants';

import dispatcher from '../dispatcher';
import axios from 'axios';
import _ from 'lodash';

import { EventEmitter } from 'events';

class CommentsStore extends EventEmitter {
    constructor()
    {
        super(...arguments);

        this.comments = [];

        this.getCommentsBegin = this.getCommentsBegin.bind(this);
        this.getCommentsEnd = this.getCommentsEnd.bind(this);
        this.change = this.change.bind(this);
        this.showComments = this.showComments.bind(this);
        this.CommentsStoreHandleActions = this.CommentsStoreHandleActions.bind(this);
    }

   getCommentsBegin(){
        axios
            .get('../data/comments_data.json')
            //.get('http://localhost:8888/store/listcomments')
            .then((response) => {
                let { data } = response;

                dispatcher.dispatch(
                    {
                        type: GET_COMMENTS_END,
                        payload: data
                    }
                );
            });
    }

    getCommentsEnd(comments)
    {
        this.comments = comments;
        this.change();
    }

    change()
    {
        this.emit('change', this.comments);
    }

    showComments()
    {
        return this.comments;
    }

    addComment(comment)
    {
        this.comments.push(comment);
        this.change();
    }

    updateComment(comment, id)
    {
        let currentCmment = _.find(this.comments,{id: id});
        let currentIndx = _.indexOf(this.comments, currentCmment);
        this.comments.splice(currentIndx, 1, comment);
        this.change();
    }


    delComment(id)
    {
        let currentComment = _.find(this.comments,{id: id});
        let currentIndex = this.comments.indexOf(currentComment);
        this.comments.splice(currentIndex, 1);
        this.change();
    }

    CommentsStoreHandleActions(action)
    {
        //console.log("получен Action:", action);
        switch (action.type)
        {
            case ADD_COMMENT:
            {
                this.addComment(action.payload);
                break;
            }

            case UPDATE_COMMENT:
            {
                this.updateComment(action.payload, action.payloadID);
                break;
            }

            case GET_COMMENTS_BEGIN:
            {
                this.getCommentsBegin();
                break;
            }
            case GET_COMMENTS_END:
            {
                this.getCommentsEnd(action.payload);
                break;
            }
            case DEL_COMMENT:

            {   //console.log(action.payload);
                this.delComment(action.payload);
                break;
            }

        }
    }
}

const commentsStore = new CommentsStore;

dispatcher.register(commentsStore.CommentsStoreHandleActions);

export default commentsStore;
