import { Injectable } from '@angular/core';
import { CallService, CrudService } from 'componentex';

@Injectable()
export class TareaService extends CrudService {

    public static AUDIO = 2;
    public static FOTO = 1;

    constructor(protected _cl: CallService) {
        super(_cl, 'operacion/tarea/');
    }

}
