import { Injectable } from '@angular/core';
import { CallService, CrudService } from '../../shared';

@Injectable()
export class TipoclienteService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'operacion/tipo/');
        this.redirectUrl = 'configuracion/tipo/cliente/'
    }

}
