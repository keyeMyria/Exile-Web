import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
import { CommonModule } from '@angular/common';
// import { FormsModule, ReactiveFormsModule } from '@angular/forms';
// import { APP_BASE_HREF } from '@angular/common';
import { CallService } from './call.service';
import { AppRouteModule } from './app.route.module';
import { AppComponent } from './app.component';
import { LoaderComponent } from './conponent-lib/loader/loader.component';
import { BaseComponent } from './containers/pages/base/base.component';
import { AuthComponent } from './containers/pages/auth/auth.component';

// import { SidebarModule } from './sidebar/sidebar.module';
// import { FooterModule } from './shared/footer/footer.module';
// import { NavbarModule} from './shared/navbar/navbar.module';

@NgModule({
    imports: [
        BrowserModule,
        HttpModule,
        CommonModule,
        AppRouteModule
    ],
    declarations: [
        AppComponent,
        LoaderComponent
    ],
    providers: [
        CallService
    ],
    bootstrap: [AppComponent]
})

export class AppModule { }
