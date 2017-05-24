import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { APP_BASE_HREF } from '@angular/common';

import { AppComponent } from './app.component';
import { AppRoutes } from './app.routing';
import { LoaderComponent } from './conponent-lib/loader/loader.component';

import { DashboardComponent } from './containers/pages/dashboard/dashboard.component';
import { AuthComponent } from './containers/pages/auth/auth.component';

// import { SidebarModule } from './sidebar/sidebar.module';
// import { FooterModule } from './shared/footer/footer.module';
// import { NavbarModule} from './shared/navbar/navbar.module';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        RouterModule.forRoot(AppRoutes),
        HttpModule
    ],
    declarations: [
        AppComponent,
        LoaderComponent,
        DashboardComponent,
        AuthComponent
    ],
    bootstrap: [AppComponent]
})

export class AppModule { }
