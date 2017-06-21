import React from 'react';
import {addComment} from '../actions/commentsActions';


export default class commentForm extends React.Component {

    constructor() {
        super(...arguments);
        this.addNewComment = this.addNewComment.bind(this);
    }

    addNewComment()
    {
        let i = this.props.length;
        let postId = i++;
        let id = i++;
        let name = $('#comment-author').val();
        let email = $('#comment-email').val();
        let comm = $('#comment-text').val();
        if (name.trim() && email.trim() && comm.trim()){
            addComment({postId, id, name, email, comm});
            $('#comment-Form')[0].reset();
        }
    }

    render() {
        let user = window.localStorage.getItem('login');
        return (
            <form className={user ? 'form-horizontal': 'none'} id="comment-Form">
                <div className="form-group">
                    <div className="col-sm-8" id="col-sm8">
                        <label className="inputForm">Добавить комментарий:</label><br/>
                        <input type='text' className="form-control" defaultValue='' placeholder='Ваше имя...' id='comment-author' required="required"/><br/>
                        <input type='text' className="form-control"  defaultValue='' placeholder='Ваш e-mail...' id='comment-email' required="required"/><br/>
                        <textarea className="form-control" defaultValue='' placeholder='Текст комментария...' id='comment-text' required="required" rows="5"/><br/>
                        <button type="button" className='btn btn-info' onClick={this.addNewComment}>Добавить</button>
                    </div>
                </div>
            </form>
        );
    }
}