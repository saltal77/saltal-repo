import React from 'react';

export default class AdressMap extends React.Component {
    constructor() {
        super(...arguments);
    }

    render() {
        const url = 'https://yandex.ru/maps/?um=constructor:ijZjw62YUqiiwDf-cLYYyptRFWAeLZ1w&amp;source=' +
            'constructorStatic"target="_blank">';

        const url_img = 'https://api-maps.yandex.ru/services/constructor/1.0/static/' +
            '?sid=ijZjw62YUqiiwDf-cLYYyptRFWAeLZ1w&amp;width=600&amp;height=450&amp;' +
            'lang=ru_RU&amp;sourceType=constructor"alt=""style="border: 0; width: 30%; height: 374px;';

        return (
            <div className="col-md-10" >
                <a href={url}> <img src = {url_img}/></a>

            </div>);
    }
}
