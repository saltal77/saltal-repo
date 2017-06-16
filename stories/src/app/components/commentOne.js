import React from 'react';
import {Link} from 'react-router';
import {delComment, updateComment } from '../actions/commentsActions';


export default class CommentOne extends React.Component {
    constructor() {
        super(...arguments);

        this.state = {
            Edit: false
        };

        this.delCmment = this.delCmment.bind(this);
        this.toEdit = this.toEdit.bind(this);
        this.changeCmment = this.changeCmment.bind(this);
    }

    toEdit(e){
        e.preventDefault();
        this.setState({Edit: !this.state.Edit},  () => {
            //console.log('сотояние this.state.Edit: ', this.state.Edit)
        });
    };

   delCmment(){
       let id = this.props.id;
       delComment(id);
    }

    changeCmment(){
        let postId = this.props.postId;
        let id = this.props.id;
        let name = $('#edit-comment-author').val();
        let email = $('#edit-comment-email').val();
        let comm = $('#edit-comment-text').val();
        if (name.trim() && email.trim() && comm.trim()){
            updateComment({postId, id, name, email, comm});
            $('#edit-comment-Form')[0].reset();
        }
        this.setState({Edit: !this.state.Edit});
    }

    render() {
        return (
            <div className="col-md-11">
                <h3>{this.props.name}</h3>
                <p>{this.props.email}</p>
                <p>{this.props.comm}</p>
                <Link  to={ "/#marker" + this.props.postId }>читать рассказ...</Link>

                {/*Отображается в случае нажатия на "Редактировать" выставляя нужные значения id на полях input*/}
                <form className={this.state.Edit ? 'form-horizontal': 'none'}  id={this.state.Edit ? 'edit-comment-Form': 'none'}>
                    <div className="form-group">
                        <div className="col-sm-8" id={this.state.Edit ? 'edit-col-sm-8' : 'none'}>
                            <label className="inputForm">Редактирование:</label><br/>
                            <input type='text' className="form-control" defaultValue={this.props.name} id={this.state.Edit ? 'edit-comment-author' : 'none'} placeholder='Ваше имя...'/><br/>
                            <input type='text' className="form-control"  defaultValue={this.props.email}  id={this.state.Edit ? 'edit-comment-email' : 'none'} placeholder='Ваш e-mail...'/><br/>
                            <textarea className="form-control" defaultValue={this.props.comm} id={this.state.Edit ? 'edit-comment-text' : 'none'} rows="3" placeholder='Текст комментария...'/><br/>
                            <button type="button" className='btn btn-default' onClick={this.changeCmment}>Сохранить</button>
                        </div>
                    </div>
                </form>


                <button className="btn btn-default" onClick={this.toEdit}>Редактировать</button>
                <button className="btn btn-default" onClick={this.delCmment}>Удалить</button>
            </div>
        );
    }
}
