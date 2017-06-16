import dispatcher from '../dispatcher';
import {ADD_COMMENT, GET_COMMENTS_BEGIN, DEL_COMMENT, UPDATE_COMMENT} from '../constants/commentsConstants';

export function addComment({postId, id, name, email, comm}) {
    const comment = {postId, id, name, email, comm};

    dispatcher.dispatch({
        type: ADD_COMMENT,
        payload: comment
    });
}

export function getComments() {
    dispatcher.dispatch({
        type: GET_COMMENTS_BEGIN
    });
}

export function delComment(id) {
    dispatcher.dispatch({
        type: DEL_COMMENT,
        payload: id
    });
}


export function updateComment({postId, id, name, email, comm}) {
    const updComment = {postId, id, name, email, comm};

    dispatcher.dispatch({
        type: UPDATE_COMMENT,
        payload: updComment,
        payloadID: id
    });
}