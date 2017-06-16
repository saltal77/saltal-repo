import React from 'react';
import { Link } from 'react-router';


export default class NotFound extends React.Component {

    render() {
        return (
            <div className='col-md-11'>
                    <div className='col-md-11'>
                        <h3>Ошибка 404. Страница не найдена.</h3>
                        <Link className="btn btn-info authorinfo" to="/redirect">На Главную</Link>
                    </div>
            </div>
        )
    }
}
