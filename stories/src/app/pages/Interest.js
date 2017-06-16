import React from 'react';
import InterestList from '../components/interestList';
import InterestStore from '../stores/interestStore';
import {getInterest} from '../actions/interestActions';
import InterestForm from '../components/interestForm';


export default class Interest extends React.Component {
    constructor() {
        super(...arguments);

        this.state = {
            interestArray: []
        };

        this.onInterestChange = this.onInterestChange.bind(this);

    }

    onInterestChange(interestArray)
    {
        this.setState({
            interestArray
        });
    }

    componentDidMount()
    {
        getInterest();
    }

    componentWillMount(){
        InterestStore.on('change', this.onInterestChange);
    }

    componentWillUnmount()
    {
        InterestStore.removeListener('change', this.onInterestChange);

    }

    render() {
        return(
            <div className="col-md-12 fox">
                <div className="col-md-10">
                    <h3>Кое что интересное...</h3>
                    {!this.props.children ? (<InterestList interest={this.state.interestArray} />): (this.props.children)}
                    <InterestForm />
                </div>
            </div>
        );
    }
}


