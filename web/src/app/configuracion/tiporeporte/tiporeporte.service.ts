import { Injectable } from '@angular/core';
import { CallService, CrudService } from 'componentex';

@Injectable()
export class TipoReporteService extends CrudService {

    constructor(protected _cl: CallService) {
        super(_cl, 'novedades/tipo/');
        this.redirectUrl = 'configuracion/tipo/reporte/'
    }

}
