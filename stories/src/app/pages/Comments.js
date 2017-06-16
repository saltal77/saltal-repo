import React from 'react';
import CommentList from '../components/CommentList';
import CommentsStore from '../stores/commentsStore';
import {getComments} from '../actions/commentsActions';
import Form from '../components/commentForm'


export default class Comments extends React.Component {
    constructor() {
        super(...arguments);

        this.state = {
            comments: []
        };

        this.onCommentChange = this.onCommentChange.bind(this);

    }

    onCommentChange(comments) // приходит - this.comments из Store по подписке на событие сhange в commentsStore
                             // (this.emit('change', this.comments);)
    {
        //console.log(comments);
        this.setState({
            comments
        });
    }

    componentDidMount()
    {
        getComments();
    }


    componentWillMount(){
        CommentsStore.on('change', this.onCommentChange);
    }

    componentWillUnmount()
    {
        CommentsStore.removeListener('change', this.onCommentChange);

    }

    render() {
        return(
            <div className="col-md-12 fox">
                <div className="col-md-11">
                    <h3>Некоторые мысли по поводу рассказов...</h3>
                    {!this.props.children ? (<CommentList comments={this.state.comments} />): (this.props.children)}
                    <Form length={this.state.comments.length}/>
                </div>
            </div>
        );
    }
}

