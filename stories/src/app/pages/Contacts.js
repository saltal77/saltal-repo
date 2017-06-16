import React  from 'react';
import {Link} from 'react-router';
import AdressMap from '../components/AdressMap';


export default class Contacts extends React.Component {
    constructor() {
        super(...arguments);
        ////*1
        // this.routerWillLeave = this.routerWillLeave.bind(this);
    }

    // // * 2 Подтверждение перехода на другую страницу через prompt
    // componentDidMount() {
    //    this.context.router.setRouteLeaveHook(this.props.route, this.routerWillLeave);
    //     //console.log(this.props.route , this.context.router);
    // }
    //
    // routerWillLeave() {
    //     let answer = window.confirm('Вам точно нужно на эту Страницу?');
    //     if (!answer) return false
    // }

    render() {
        return (
            <div className="col-md-12 fox">
                <h3>Наш адрес:</h3>
                <div className="col-md-2">
                    <h3>Для писем: 127400, г.Москва, Декабристов ул. 1 а/я 10</h3>
                    <Link className="btn btn-info" to="/redirect">На Главную</Link>
                </div>
                <div className="col-md-10">
                    <AdressMap />
                </div>
            </div>
        );
    }
}

//// *3
// Contacts.contextTypes = {
//     router: React.PropTypes.object.isRequired
//  };