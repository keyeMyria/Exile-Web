import { Injectable } from '@angular/core';
import { CallService, CrudService } from '../../shared';

@Injectable()
export class EmpleadoService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'usuarios/empleado/');
        this.redirectUrl = 'usuarios/empleado/'
    }

}
