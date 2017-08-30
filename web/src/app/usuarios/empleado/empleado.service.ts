import { Injectable } from '@angular/core';
import { CallService, CrudService } from 'componentex';

@Injectable()
export class EmpleadoService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'usuarios/empleado/');
        this.redirectUrl = 'usuarios/empleado/'
    }

}
