import React, { Component } from 'react';
import axios from 'axios';
import Post from './post'
import Form from './storyForm'
import EventEmitter from 'wolfy87-eventemitter';

window.ee = new EventEmitter();


export default class blogsContent extends Component {

    constructor() {
        super(...arguments);

        this.state = {
            stories: []
        };

        axios
            .get('../data/stories_data.json')
            //.get('http://localhost:8888/store/liststories')
            .then((responce) => {
                let { data } = responce;

                this.setState({
                    stories: data
                });
            });
    }

    componentDidMount() {
        window.ee.addListener('Story.add', (newStory) => {
            let newData = newStory.concat(this.state.stories);
            this.setState({stories: newData});
        });
    }

    render(){

        let story = this.state.stories.map((story, index) => {return(
            <div className="col-md-11" key={index}>
                <Post data={story} />
            </div>)
        });

        if (!this.state.stories.length){
            story = <h3> Контент редактируется </h3>
        }

        return (
            <div className="col-md-12 fox">
                {story}
                <p className={'hist_counter '+(this.state.stories.length > 0 ? '':'none')}>Историй: {this.state.stories.length}</p>
                <div className="col-md-10 form-stories">
                    <details open="open">
                        <summary>Добавить...</summary>
                <Form length = {this.state.stories.length }/>
                    </details>
                </div>
            </div>
        );
    }
}




// // Old blogsContent
// let blogsContent = React.createClass({
//     getInitialState: function(){
//         return {
//             showPost: true
//         };
//     },
//     getDefaultProps: function () {
//         return {
//             title: 'Нет Назания',
//             text: 'Нет текста'
//         };
//     },
//     render: function() {
//
//         let story = this.props.stories.map((story, index) => {
//             return (
//                 <div className="col-md-10" key={index}>
//                 <h3>{story.title}</h3>
//                 <p>{story.text}</p>
//                 </div>);
//         });
//         let posts;
//         if(this.state.showPost){
//             posts = story
//         }
//         return (
//             <div className="col-md-11 ">
//                 {posts}
//                 <p>{this.props.text}</p>
//              <strong>Всего историй: {posts.length}</strong>
//             </div>
//         );
//     }
// });
// export default blogsContent








