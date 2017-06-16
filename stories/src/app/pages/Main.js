import React from 'react';
import Blogs_content from './../components/blogsContent';


export default class Main extends React.Component {

    constructor() {
        super(...arguments);
    }

    render(){
        return(
            <div className="row">
                <Blogs_content />
            </div>
        )
    }
}

