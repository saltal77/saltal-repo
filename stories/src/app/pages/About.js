import React from 'react';
import AuthorsList from '../components/authorsList';


export default class About extends React.Component {
    constructor() {
        super(...arguments);
    }

    render() {
        return (
            <div className="col-md-12 fox">
                    {!this.props.children ? (<AuthorsList/>): (this.props.children)}
            </div>
        );
    }
}
