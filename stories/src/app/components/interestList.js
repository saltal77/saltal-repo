import React from 'react';
import InterestOne from './interestOne';


export default class InterestList extends React.Component {
    constructor() {
        super(...arguments);
    }

    render() {
        if(!this.props.interest.length)
            return null;

        let intrst = this.props.interest.map((data, index) => {
            return <InterestOne key={index} {...data} />
        });

        return (
            <div className="col-md-11">
                {intrst}
            </div>
        );
    }
}
