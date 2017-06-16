import React, { Component } from 'react';
import H1_menu from './menuHeader';
import Nav_menu from './menuNavbar'


export default class ContainerMenu extends Component {

    render(){
        return (
            <div className="page-header">
                <H1_menu />
                <Nav_menu />
            </div>
        );
    }
}



