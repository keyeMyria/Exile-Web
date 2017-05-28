import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
// import { FormsModule, ReactiveFormsModule } from '@angular/forms';
// import { APP_BASE_HREF } from '@angular/common';
import { CallService } from './call.service';
import { AppRouteModule } from './app.route.module';
import { AppComponent } from './app.component';
import { LoaderComponent } from './conponent-lib/loader/loader.component';
import { DashboardComponent } from './containers/pages/dashboard/dashboard.component';
import { AuthComponent } from './containers/pages/auth/auth.component';

// import { SidebarModule } from './sidebar/sidebar.module';
// import { FooterModule } from './shared/footer/footer.module';
// import { NavbarModule} from './shared/navbar/navbar.module';

@NgModule({
    imports: [
        BrowserModule,
        // FormsModule,
        // ReactiveFormsModule,
        HttpModule,
        AppRouteModule
    ],
    declarations: [
        AppComponent,
        LoaderComponent,
        DashboardComponent,
        AuthComponent
    ],
    providers: [
        CallService
    ],
    bootstrap: [AppComponent]
})

export class AppModule { }
