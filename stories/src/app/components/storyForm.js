import React from 'react';
import ReactDOM from 'react-dom';


export default class Form extends React.Component {

    constructor() {
        super(...arguments);

        this.addNewStory = this.addNewStory.bind(this);
    }

    addNewStory(e) {
        e.preventDefault();
        let id = this.props.length + 1;
        let author = ReactDOM.findDOMNode(this.refs.author).value;
        let title = ReactDOM.findDOMNode(this.refs.title).value;
        let text = ReactDOM.findDOMNode(this.refs.text).value;
        let text_next = '';
        if (text.length > 320){
            text_next = text.substring(321, );
            text = text.substring(0, 321)+ '...';
        }
        if (author.trim() && title.trim() && text.trim()){
            let newStory = [{id: id, title: title, text: text, text_next: text_next, author: author}];
            window.ee.emit('Story.add', newStory);
            ReactDOM.findDOMNode(this.refs.author).value = '';
            ReactDOM.findDOMNode(this.refs.title).value = '';
            ReactDOM.findDOMNode(this.refs.text).value = '';
        }
    }

    render() {
        let user = window.localStorage.getItem('login');
        return (
            <form className={user ? 'form-horizontal': 'none'}>
                <div className="form-group">
                    <div className="col-sm-10">
                <label className="inputForm">Добавить Историю:</label><br/>
                <input type='text' className="form-control" defaultValue='' placeholder='Ваше имя...' ref='author' required="required"/><br/>

                <input type='text' className="form-control"  defaultValue='' placeholder='Тема рассказа...' ref='title' required="required"/><br/>
                <textarea className="form-control" defaultValue='' placeholder='Текст...' ref='text' required="required" rows="5"/><br/>
                <button type="submit" className='btn btn-info' onClick={this.addNewStory}>Добавить</button>
                    </div>
                </div>
            </form>
        );
    }
}