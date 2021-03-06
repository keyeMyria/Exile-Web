import { Injectable } from '@angular/core';
import { CallService, CrudService } from '../../shared';

@Injectable()
export class ClienteService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'operacion/cliente/');
    }

}
