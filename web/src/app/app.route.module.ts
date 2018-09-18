import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { AppRoutes } from './app.routing';

// import { SelectiveStrategy } from './selective-strategy.service';
@NgModule({
    imports: [
        RouterModule.forRoot(AppRoutes, { useHash: true })
    ],
    exports: [RouterModule]
})
export class AppRouteModule { }
