import { Injectable } from '@angular/core';
import { CallService, CrudService } from 'componentex';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class NotificacionService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'operacion/notificacion/');
        this.conf.add = null;
        this.conf.delete = null;
        this.conf.edit = null;
        this.conf.redirect = null;
    }

    /**
     * coloca estado de completado a una notificacion
     * @param  {any} mgs (notificacion:uk , latitud, longitud, [descompletado=true], [descompletado_por], [fecha=now])
     * @return {Observable<any>}
     */
    completado(mgs): Observable<any> {
        return this._cl.post('operacion/completado/form/', mgs);
    }

    /**
     * coloca estado de descompletado a una notificacion
     * @param  {number} id id de la notificacion
     * @return {Observable<nay>}    [description]
     */
    descompletado(id: number): Observable<any> {
        return this._cl.delete(`operacion/completado/delete/${id}/`);
    }


}
