import React from 'react';
import axios from 'axios';
import Author from './author';


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

        let authors = this.state.so_authors.map((author, index) => {
            return <Author key={index} {...author} />
        });

        return (
            <div className="col-md-11">
                <h3>Наши авторы</h3>
                {authors}
            </div>
        );
    }
}