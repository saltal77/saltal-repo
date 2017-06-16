import React from 'react';
import axios from 'axios';
import AuthorOne from './authorOne'


export default class AuthorsList extends React.Component {
    constructor() {
        super(...arguments);

        this.state = {
            so_authors: []

        };

        axios
            .get('../data/authors_data.json')
            //.get('http://localhost:8888/store/listauthors/')
            .then((responce) => {
                let { data } = responce;

                this.setState({
                    so_authors: data
                });
            });
    }

    render() {
        if(!this.state.so_authors.length)
            return null;

        let objAuthor = this.state.so_authors.filter((author)=>{
            return author.id == this.props.params.authorId
        });

        let Author = objAuthor.map((author, index) =>{
            return <AuthorOne key={index} {...author} />
        });

        return (
            <div className="col-md-11">
                <h3>Некоторые детали ...</h3>
                {Author}
            </div>

        );
    }
}