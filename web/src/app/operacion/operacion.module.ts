import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SampleModule } from 'componentex';
import { OperacionRoutes } from './route';

import { TipoclienteListComponent } from './tipocliente/tipocliente.component';
import { TipoclienteService } from './tipocliente/tipocliente.service';
@NgModule({
    imports: [
        CommonModule,
        SampleModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule.forChild(OperacionRoutes)
    ],
    declarations: [
        TipoclienteListComponent
    ],
    providers: [
        TipoclienteService
    ]
})
export class OperacionModule { }
