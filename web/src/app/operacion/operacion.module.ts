import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SampleModule } from 'componentex';
import { OperacionRoutes } from './route';

import { TipoclienteComponent } from './tipocliente/tipocliente.component';

@NgModule({
    imports: [
        CommonModule,
        SampleModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule.forChild(OperacionRoutes)
    ],
    declarations: [
        TipoclienteComponent
    ]
})
export class OperacionModule { }
