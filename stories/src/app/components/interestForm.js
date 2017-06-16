import React from 'react';
import {addInterest} from '../actions/interestActions';
import {Link} from 'react-router';

export default class interestForm extends React.Component {

    constructor() {
        super(...arguments);
        this.addNewInterest = this.addNewInterest.bind(this);
    }

    addNewInterest()
    {
        let title = $('#interest-title').val();
        let text = $('#interest-text').val();
        if (title.trim() && text.trim()){
            addInterest({title, text});
            $('#interest-Form')[0].reset();
        }
    }

    render() {
        return (
            <form className="form-horizontal" id="interest-Form">
                <div className="form-group">
                    <div className="col-sm-10">
                        <label className="inputForm">Добавить:</label><br/>
                        <input type='text' className="form-control" defaultValue='' placeholder='Тема...' id='interest-title' required="required"/><br/>
                        <textarea className="form-control" defaultValue='' placeholder='Ваш интересный факт...' id='interest-text' required="required" rows="5"/><br/>
                        <Link className="btn btn-info" to="/about">Об авторах</Link>
                        <button type="button" className='btn btn-info' onClick={this.addNewInterest}>Добавить</button>
                    </div>
                </div>
            </form>
        );
    }
}
