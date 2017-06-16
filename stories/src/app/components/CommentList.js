import React from 'react';
import Comment from './commentOne';


export default class CommentList extends React.Component {
    constructor() {
        super(...arguments);
    }

    render() {
        if(!this.props.comments.length)
            return null;

        let commnt = this.props.comments.map((commnt, index) => {
            return <Comment key={index} {...commnt} />
        });

        return (
            <div className="col-md-11">
                {commnt}
            </div>
        );
    }
}