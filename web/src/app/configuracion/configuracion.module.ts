import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SampleModule } from '../shared';
import { ConfiguracionRoutes } from './route';
import { DateValueAccessorModule } from 'angular-date-value-accessor';

import { TipoclienteListComponent, TipoclienteEditComponent } from './tipocliente/tipocliente.component';
import { TipoclienteService } from './tipocliente/tipocliente.service';

import { CargoListComponent, EditCargoComponent } from './cargo/cargo.component';
import { CargoService } from './cargo/cargo.service';
import { ListGrupoComponent, EditGrupoComponent } from './grupo/grupo.component';
import { GrupoService } from './grupo/grupo.service';
import { EmpleadoService } from '../usuarios/empleado/empleado.service';
import { TipoReporteEditComponent, TipoReporteListComponent } from './tiporeporte/tiporeporte.component';
import { TipoReporteService } from './tiporeporte/tiporeporte.service';

@NgModule({
    imports: [
        CommonModule,
        SampleModule,
        FormsModule,
        ReactiveFormsModule,
        DateValueAccessorModule,
        RouterModule.forChild(ConfiguracionRoutes)

    ],
    declarations: [
        TipoclienteListComponent,
        TipoclienteEditComponent,
        CargoListComponent,
        EditCargoComponent,
        ListGrupoComponent,
        EditGrupoComponent,
        TipoReporteEditComponent,
        TipoReporteListComponent
    ],
    providers: [
        TipoclienteService,
        CargoService,
        GrupoService,
        EmpleadoService,
        TipoReporteService
    ]
})
export class ConfiguracionModule { }
