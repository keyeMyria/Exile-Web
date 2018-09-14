import { Injectable } from '@angular/core';
import { CallService, CrudService } from '../../shared';

@Injectable()
export class CargoService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'usuarios/cargo/');
        this.redirectUrl = 'usuarios/cargos/'
    }

}
