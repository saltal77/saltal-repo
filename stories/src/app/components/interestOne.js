import React from 'react';


export default class InterestOne extends React.Component {
    constructor() {
        super(...arguments);
    }

    render() {
        return (
            <div className="col-md-11">
                <h3>{this.props.title}</h3>
                <p>{this.props.text}</p>
            </div>
        );
    }
}


