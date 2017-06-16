import React from 'react';
import {Link} from 'react-router';

export default class AuthorOne extends React.Component {
    constructor() {
        super(...arguments);
    }

    render() {
        return (
            <div className="col-md-11">
                <h3>{this.props.name}</h3>
                <p>{this.props.desc}</p>
                <p>{this.props.prof}</p>
                <p>{this.props.address}</p>
                <Link className="btn btn-info authorinfo" to="/about">Назад</Link>
            </div>
        );
    }
}
