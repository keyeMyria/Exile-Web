import { Injectable } from '@angular/core';
import { CallService, CrudService } from 'componentex';

@Injectable()
export class AdminService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'usuarios/administrador/');
        this.redirectUrl = 'usuarios/admin/'
    }

}
