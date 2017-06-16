import React from 'react';
import {Link} from 'react-router';

export default class Author extends React.Component {
    constructor() {
        super(...arguments);
    }

    render() {
        return (
            <div className="col-md-11">
                    <h3><Link to={"/about/" + this.props.id}>{this.props.name}</Link></h3>
                    <p>{this.props.email}</p>
                    <p>{this.props.address}</p>
                    <p>{this.props.phone}</p>
            </div>
        );
    }
}