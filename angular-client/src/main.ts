import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideHttpClient } from '@angular/common/http'; // Alteração aqui

bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient() 
  ]
});