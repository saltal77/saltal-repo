import React, { Component } from 'react';


export default class ContainerFooter extends Component {

    render(){

        let newDate = new Date();

        return (
            <div className="modal-footer">
                &copy; {newDate.getFullYear()} <span>saltal</span>
            </div>
        );
    }
}


