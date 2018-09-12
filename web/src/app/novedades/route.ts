import { Routes } from '@angular/router';
import { MenuMeta, RouteComponent } from '../shared';
import { ReportesListComponent, EditReporteComponent } from './reportes/reportes.component';
import { ReportesService } from './reportes/reportes.service';

export const NovedadesRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'reportes', component: RouteComponent, data: { miga: 'Reportes' }, children: [
                    { path: '', component: ReportesListComponent },
                    { path: ':id/edit', component: EditReporteComponent, data: { miga: 'Editar' }, resolve: { item: ReportesService } }

                ]
            }
        ]
    }
]

export const NovedadesMenuMeta: MenuMeta[] = [
    { title: 'Reportes', url: '/novedades/reportes', icon: 'report' }
]
