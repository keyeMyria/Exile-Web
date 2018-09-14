import { Routes } from '@angular/router';
import { MenuMeta, RouteComponent } from '../shared';
import { TipoclienteListComponent, TipoclienteEditComponent } from './tipocliente/tipocliente.component';
import { TipoclienteService } from './tipocliente/tipocliente.service';
import { CargoListComponent, EditCargoComponent } from './cargo/cargo.component';
import { ListGrupoComponent, EditGrupoComponent } from './grupo/grupo.component';
import { CargoService } from './cargo/cargo.service';
import { GrupoService } from './grupo/grupo.service';
import { TipoReporteEditComponent, TipoReporteListComponent } from './tiporeporte/tiporeporte.component';
import { TipoReporteService } from './tiporeporte/tiporeporte.service';


export const ConfiguracionRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'tipo/cliente', component: RouteComponent, data: { miga: 'Tipo de cliente' }, children: [
                    { path: '', component: TipoclienteListComponent },
                    {
                        path: ':id/edit', component: TipoclienteEditComponent,
                        data: { miga: 'Editar' },
                        resolve: { item: TipoclienteService }
                    }
                ]
            },
            {
                path: 'tipo/reporte', component: RouteComponent, data: { miga: 'Tipo de reporte' }, children: [
                    { path: '', component: TipoReporteListComponent },
                    {
                        path: ':id/edit', component: TipoReporteEditComponent,
                        data: { miga: 'Editar' },
                        resolve: { item: TipoReporteService }
                    }
                ]
            },
            {
                path: 'cargo', component: RouteComponent, data: { miga: 'Cargo' }, children: [
                    { path: '', component: CargoListComponent },
                    { path: ':id/edit', component: EditCargoComponent, data: { miga: 'Editar' }, resolve: { item: CargoService } }
                ]
            },
            {
                path: 'grupo', component: RouteComponent, data: { miga: 'Grupo' }, children: [
                    { path: '', component: ListGrupoComponent },
                    { path: ':id/edit', component: EditGrupoComponent, data: { miga: 'Editar' }, resolve: { item: GrupoService } }
                ]
            }

        ]
    }

];

export const ConfiguracionMenuMeta: MenuMeta[] = [
    { title: 'Tipos de cliente', url: '/configuracion/tipo/cliente' },
    { title: 'Tipos de reporte', url: '/configuracion/tipo/reporte' },
    { title: 'Cargos', url: '/configuracion/cargo', icon: 'turned_in' },
    { title: 'Grupo', url: '/configuracion/grupo', icon: 'group' },

];
