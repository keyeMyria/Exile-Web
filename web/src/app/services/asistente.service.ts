import { CallService } from './call.service';
import { Injectable } from '@angular/core';

@Injectable()
export class AsistenteService {

    constructor(public _cl: CallService) { }

    list() {
        const query = {
            page: 1,
            num_page: 10,
            sort_property: 'noc',
            sort_direction: 'asc',
            q: ''
        };
        return this._cl.get('usuarios/asistente/list/', query, this._cl.json);
    }
    add(body: any) {
        return this._cl.post('usuarios/asistente/from/', body);
    }
    edit(id: number, body: any) {
        return this._cl.post(`usuarios/asistente/from/${id}/`);
    }
    delete(id: number) {
        return this._cl.get(`usuarios/asistente/delete/${id}/`);
    }
}
