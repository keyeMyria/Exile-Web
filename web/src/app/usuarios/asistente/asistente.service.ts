import { Injectable } from '@angular/core';
import { CallService, CrudService } from '../../shared';

@Injectable()
export class AsistenteService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'usuarios/asistente/');
    }

}
