import { Injectable } from '@angular/core';
import { CallService, CrudService } from 'componentex';

@Injectable()
export class GrupoService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'usuarios/grupo/');
        this.redirectUrl = 'usuarios/grupo/'
    }

}
