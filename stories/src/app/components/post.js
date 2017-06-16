import React, { Component } from 'react';


export default class Post extends Component {

    constructor()
    {
        super();

        this.state = {
            showPost: false
        };

        this.readMore = this.readMore.bind(this);
    }

    readMore(e){
        e.preventDefault();
        this.setState({showPost: !this.state.showPost},  () => {
            // console.log('сотояние this.state.showPost: ', this.state.showPost)
        });
    };

    render(){

        let author = this.props.data.author,
            title = this.props.data.title,
            text = this.props.data.text,
            text_next = this.props.data.text_next;

        return(

            <div className="col-md-11" id={"marker" + this.props.data.id}>
                <h3>{title}</h3>
                <p>{author}</p>
                <p>{text}</p>
                <p className={this.state.showPost ? '': 'none'}>{text_next}</p>
                <a href="#" onClick={this.readMore} className=''>читать...скрыть...</a>
                {/*<a href="#" onClick={() => this.setState({showPost: !this.state.showPost,})} className=''>Подробнее</a>*/}
            </div>
        )
    }
}


Post.propTypes = {
    data: React.PropTypes.object.isRequired,
   // author: React.PropTypes.string.isRequired // 'undefined' --- {story} income... - 'object'
};

// Post.defaultProps = {
//     data: {title:'История о...', text: 'Контент редактируется', author:'Модератор'}
// };
