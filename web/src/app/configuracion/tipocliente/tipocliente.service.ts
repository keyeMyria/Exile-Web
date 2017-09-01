import { Injectable } from '@angular/core';
import { CallService, CrudService } from 'componentex';

@Injectable()
export class TipoclienteService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'operacion/tipo/');
        this.redirectUrl = 'operacion/tipo/cliente/'
    }

}
