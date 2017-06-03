import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { AppRoutes } from './app.routing';
import { AuthGuard } from './services/auth.guard';
import { LibModule } from './lib/lib.module';
import { AuthComponent } from './auth/auth.component';

// import { BaseComponent } from './lib/base/base.component';
// import { P404Component } from './lib/404/404.component';
// import { SidebarComponent } from './lib/sidebar/sidebar.component';
// import { ToolbarComponent } from './lib/toolbar/toolbar.component';

@NgModule({
    imports: [
        BrowserModule,
        LibModule,
        RouterModule.forRoot(AppRoutes)
    ],
    declarations: [
        AuthComponent
    ],
    providers: [
        AuthGuard
    ],
    exports: [RouterModule]
})
export class AppRouteModule { }
