import { Injectable } from '@angular/core';
import { CallService, CrudService } from 'componentex';

@Injectable()
export class CompletadoService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'operacion/completado/');
    }
}
