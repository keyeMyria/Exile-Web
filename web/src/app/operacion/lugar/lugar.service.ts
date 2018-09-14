import { Injectable } from '@angular/core';
import { CallService, CrudService } from '../../shared';

@Injectable()
export class LugarService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'operacion/lugar/');
    }

}
