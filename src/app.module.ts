import { CacheModule, Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { GithubController } from './github/github.controller';
import { GithubService } from './github/github.service';
import { GithubModule } from './github/github.module';
import * as redisStore from 'cache-manager-redis-store';
import { ClientsModule, Transport } from '@nestjs/microservices';

@Module({
  imports: [
    CacheModule.register({
      store: redisStore,
      host: 'localhost',
      port: 6379,
      name: 'KAFKA_SERVICE',
        transport: Transport.KAFKA,
        options: {
          client: {
            brokers: ['localhost:9092'],
    },
      },
    }),
    GithubModule,
  ],
  controllers: [AppController, GithubController],
  providers: [AppService, GithubService],
})
export class AppModule {}
