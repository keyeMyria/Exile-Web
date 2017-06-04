import { Routes } from '@angular/router';

import { EstadisticasComponent } from './estadisticas/estadisticas.component';
import { ExportacionComponent } from './exportacion/exportacion.component';

export const InformesRoutes: Routes = [
    {
        path: '', children: [
            { path: 'estadisticas', component: EstadisticasComponent },
            { path: 'exportacion', component: ExportacionComponent }
        ]
    }
];
