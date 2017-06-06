import { NgModule, CUSTOM_ELEMENTS_SCHEMA} from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ToolbarComponent } from './toolbar/toolbar.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { LoaderComponent } from './loader/loader.component';
import { CardComponent} from './card/card.component';
import { BaseComponent } from './base/base.component';
import { P404Component } from './404/404.component';
import { TableComponent } from './table/table.component';

const LibComponents = [
    P404Component,
    BaseComponent,
    CardComponent,
    LoaderComponent,
    SidebarComponent,
    ToolbarComponent,
    TableComponent
];

@NgModule({
    imports: [
        CommonModule,
        RouterModule,
    ],
    declarations: LibComponents,
    exports: LibComponents
})
export class LibModule { }
